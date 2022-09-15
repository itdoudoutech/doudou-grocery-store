import random, pygame

width, height, font_size = 640, 480, 15

pygame.init()
pygame.display.set_caption("黑客帝国")
font = pygame.font.Font(None, 20)
screen = pygame.display.set_mode((width, height))

bg = pygame.Surface((width, height), flags=pygame.SRCALPHA)
bg.fill(pygame.Color(0, 0, 0, 50))

# 数字
texts = [font.render(str(i), True, pygame.Color("#00FF00")) for i in range(2)]
columns = int(width / font_size)
rows = [0 for i in range(columns)]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    pygame.time.delay(50)
    screen.blit(bg, (0, 0))

    for i in range(len(rows)):
        text = random.choice(texts)
        screen.blit(text, (i * font_size, rows[i] * font_size))
        rows[i] += -1 * rows[i] if rows[i] * font_size > height or random.random() > 0.9 else 1

    pygame.display.update()
