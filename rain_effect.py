import pygame
import random

# 初始化pygame
pygame.init()

# 设置窗口尺寸
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("下雨效果")

# 水花类
class Splash:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.droplets = []
        num_droplets = random.randint(3, 8)  # 随机水滴数量
        for _ in range(num_droplets):
            angle = random.uniform(0, 2 * 3.1415926)
            speed = random.uniform(2, 6)
            dx = speed * pygame.math.Vector2(1, 0).rotate_rad(angle).x
            dy = speed * pygame.math.Vector2(1, 0).rotate_rad(angle).y
            size = random.randint(1, 3)
            color = (random.randint(0, 50), random.randint(0, 50), 255)
            self.droplets.append({
                'x': x,
                'y': y,
                'dx': dx,
                'dy': dy,
                'size': size,
                'color': color,
                'alpha': 255
            })

    def update(self):
        to_remove = []
        for droplet in self.droplets:
            droplet['x'] += droplet['dx']
            droplet['y'] += droplet['dy']
            droplet['alpha'] -= 10
            if droplet['alpha'] <= 0:
                to_remove.append(droplet)
        for droplet in to_remove:
            self.droplets.remove(droplet)
        return len(self.droplets) == 0

    def draw(self):
        for droplet in self.droplets:
            surface = pygame.Surface((droplet['size'] * 2, droplet['size'] * 2), pygame.SRCALPHA)
            pygame.draw.circle(surface, (droplet['color'][0], droplet['color'][1], droplet['color'][2], droplet['alpha']),
                               (droplet['size'], droplet['size']), droplet['size'])
            screen.blit(surface, (int(droplet['x'] - droplet['size']), int(droplet['y'] - droplet['size'])))

# 雨滴类
class Raindrop:
    def __init__(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-HEIGHT, 0)
        self.speed = random.randint(10, 30)  # 增加速度范围
        self.length = random.randint(10, 30)
        self.thickness = random.randint(1, 3)  # 增加雨滴粗细变化
        self.color = (random.randint(0, 100), random.randint(0, 100), 255)  # 增加颜色变化

    def fall(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-HEIGHT, 0)
            self.x = random.randint(0, WIDTH)
            return True
        return False

    def draw(self):
        pygame.draw.line(screen, self.color, (self.x, self.y), (self.x, self.y + self.length), self.thickness)

# 创建雨滴列表
raindrops = []
for _ in range(100):  # 增加雨滴数量
    raindrop = Raindrop()
    raindrops.append(raindrop)

# 创建水花列表
splashes = []

# 主循环
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))

    # 更新和绘制雨滴
    for raindrop in raindrops:
        if raindrop.fall():
            splashes.append(Splash(raindrop.x, HEIGHT))
        raindrop.draw()

    # 更新和绘制水花
    to_remove = []
    for splash in splashes:
        if splash.update():
            to_remove.append(splash)
        else:
            splash.draw()

    # 移除消失的水花
    for splash in to_remove:
        splashes.remove(splash)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()