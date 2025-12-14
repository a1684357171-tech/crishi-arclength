import math

print("=== 戚氏弧长算法 - 早期工程实战版 ===")
print("作者：戚华建")
print("这是算法的最早起源，用于工程现场快速计算圆弧长度")
print("输入：弦高 H + 半弦长 L")
print()

H = float(input('请输入弦高 H（从弦到弧顶的垂直距离）: '))
L = float(input('请输入半弦长 L（高垂直连接圆弧的边）: '))

if L <= 0:
    print("错误：L 必须大于0！")
else:
    # 半圆心角
    a_half = math.atan(H / L)
    # 完整圆心角（弧度）
    a = 2 * a_half
    # 半径（修正版，使用 sin(a/2)）
    r = L / math.sin(a_half)
    # 弧长
    l = a * r

    print('\n=== 计算结果 ===')
    print(f'圆心角 a: {a:.6f} 弧度（约 {math.degrees(a):.2f} 度）')
    print(f'半径 r: {r:.6f}')
    print(f'弧长 l: {l:.6f}')
    print('\n此版本为戚华建在实际工程中最先使用的快速计算方法，')
    print('是整个“戚氏弧长算法”系列的起点与灵感来源！')
