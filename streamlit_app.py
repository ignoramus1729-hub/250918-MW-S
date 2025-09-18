import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


st.title("n각형의 대각선 그리기 앱")

# n값 입력 (최소 4)
n = st.number_input("n각형의 n값을 입력하세요 (4 이상)", min_value=4, value=5, step=1)

def get_polygon_vertices(n, radius=1, center=(0,0)):
    angles = np.linspace(0, 2*np.pi, n, endpoint=False)
    return [
        (center[0] + radius * np.cos(a), center[1] + radius * np.sin(a))
        for a in angles
    ]

def get_diagonals(n):
    diagonals = []
    for i in range(n):
        for j in range(i+1, n):
            # 인접하지 않은 꼭짓점만 대각선
            if abs(i-j) != 1 and abs(i-j) != n-1:
                diagonals.append((i, j))
    return diagonals

vertices = get_polygon_vertices(n)
diagonals = get_diagonals(n)

fig, ax = plt.subplots(figsize=(5,5))
# n각형 외곽선
polygon = np.array(vertices + [vertices[0]])
ax.plot(polygon[:,0], polygon[:,1], 'k-', lw=2)
# 꼭짓점 표시
ax.scatter(polygon[:-1,0], polygon[:-1,1], color='red')
# 대각선 그리기
for i, j in diagonals:
    x = [vertices[i][0], vertices[j][0]]
    y = [vertices[i][1], vertices[j][1]]
    ax.plot(x, y, 'b--', alpha=0.7)
for idx, (x, y) in enumerate(vertices):
    ax.text(x, y, str(idx+1), fontsize=12, ha='center', va='center', color='green')
ax.set_aspect('equal')
ax.axis('off')
st.pyplot(fig)
