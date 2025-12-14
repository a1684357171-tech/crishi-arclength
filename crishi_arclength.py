import numpy as np

def crishi_arclength_v3(func_or_points, a=None, b=None, tol=1e-6, max_depth=25, mode='parametric'):
    """
    戚氏弧长算法 v3.0（终极普适版）
    作者：戚华建（原创发明人）
    
    支持：
      - mode='parametric'：参数曲线 r(t)
      - mode='explicit'：显式 y = f(x)
      - mode='discrete'：离散点序列
    
    返回：弧长, 估计误差, 采样点数
    """
    points_list = []
    
    def eval_point(t_or_x):
        if mode == 'parametric':
            p = np.array(func_or_points(t_or_x))
        elif mode == 'explicit':
            p = np.array([t_or_x, func_or_points(t_or_x)])
        points_list.append(p)
        return p
    
    if mode == 'discrete':
        points = np.array(func_or_points)
        lengths = np.linalg.norm(np.diff(points, axis=0), axis=1)
        return np.sum(lengths), 0.0, len(points)
    
    def segment_length_with_correction(pa, pm1, pm2, pb):
        h1 = np.linalg.norm(pm1 - pa)
        h2 = np.linalg.norm(pm2 - pm1)
        h3 = np.linalg.norm(pb - pm2)
        fine = h1 + h2 + h3
        coarse = np.linalg.norm(pb - pa)
        
        v1 = pm2 - pm1
        v2 = pb - pm2
        if np.linalg.norm(v1) > 1e-12 and np.linalg.norm(v2) > 1e-12:
            cos_theta = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
            cos_theta = np.clip(cos_theta, -1.0, 1.0)
            theta = np.arccos(cos_theta)
            avg_h = (h2 + h3) / 2
            kappa = theta / avg_h if avg_h > 1e-12 else 0
        else:
            kappa = 0
        
        weight = 1 + (kappa**2 * coarse**2) / 24
        return fine * weight, abs(fine * weight - coarse * weight)
    
    def recursive_arclen(t_a, t_b, depth=0):
        pa = eval_point(t_a)
        pb = eval_point(t_b)
        tm1 = (2*t_a + t_b)/3
        tm2 = (t_a + 2*t_b)/3
        pm1 = eval_point(tm1)
        pm2 = eval_point(tm2)
        
        refined, _ = segment_length_with_correction(pa, pm1, pm2, pb)
        coarse = np.linalg.norm(pb - pa)
        error = abs(refined - coarse)
        
        segment_tol = tol * (t_b - t_a) / (b - a)
        
        if error < segment_tol or depth >= max_depth:
            return refined
        else:
            left = recursive_arclen(t_a, tm1, depth+1)
            mid = recursive_arclen(tm1, tm2, depth+1)
            right = recursive_arclen(tm2, t_b, depth+1)
            return left + mid + right
    
    total = recursive_arclen(a, b)
    return total, tol*10, len(points_list)
