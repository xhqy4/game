import pygame
import random

# 初始化 Pygame
pygame.init()

# 定义屏幕尺寸
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("黑白块音游")

# 定义颜色
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 定义块的尺寸
BLOCK_WIDTH = 100
BLOCK_HEIGHT = 100

# 块列表
blocks = []

# 生成新块
def create_block():
    x = random.randint(0, 3) * BLOCK_WIDTH
    block = pygame.Rect(x, -BLOCK_HEIGHT, BLOCK_WIDTH, BLOCK_HEIGHT)
    color = random.choice([BLACK, WHITE])
    blocks.append((block, color))

# 定义判定线的位置，这里将判定线往上移动 100 像素，你可以根据需要调整这个值
JUDGE_LINE_Y = SCREEN_HEIGHT - 120

# 主游戏循环
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # 检查键盘按下事件
            for block, color in blocks[:]:
                if block.y + BLOCK_HEIGHT >= JUDGE_LINE_Y:
                    # 计算块所在的列
                    col = block.x // BLOCK_WIDTH
                    # 假设按键 1-4 对应四列
                    if event.key == pygame.K_1 and col == 0:
                        blocks.remove((block, color))
                    elif event.key == pygame.K_2 and col == 1:
                        blocks.remove((block, color))
                    elif event.key == pygame.K_3 and col == 2:
                        blocks.remove((block, color))
                    elif event.key == pygame.K_4 and col == 3:
                        blocks.remove((block, color))

    # 生成新块
    if random.random() < 0.02:
        create_block()

    # 移动块
    for block, _ in blocks[:]:
        block.y += 5
        if block.y > SCREEN_HEIGHT:
            blocks.remove((block, _))

    # 绘制背景
    screen.fill(WHITE)

    # 绘制块
    for block, color in blocks:
        pygame.draw.rect(screen, color, block)

    # 绘制判定线
    pygame.draw.line(screen, BLACK, (0, JUDGE_LINE_Y), (SCREEN_WIDTH, JUDGE_LINE_Y), 2)

    # 更新显示
    pygame.display.flip()

    # 控制帧率
    clock.tick(60)

# 退出 Pygame
pygame.quit()