import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Happy Birthday Cassandra!")

# Colors
SKY_BLUE = (135, 206, 235)
GRASS_GREEN = (34, 139, 34)
TREE_BROWN = (101, 67, 33)
WILLOW_GREEN = (107, 142, 35)
SKIN_TONE_BOY = (255, 220, 177)
SKIN_TONE_GIRL = (255, 228, 196)
KHAKI = (195, 176, 145)
NAVY_BLUE = (25, 25, 112)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN_HAIR = (101, 67, 33)
PINK = (255, 192, 203)
UDON_BOWL = (240, 230, 210)
BROTH_COLOR = (210, 180, 140)
NOODLE_COLOR = (255, 248, 220)

# Clock for controlling frame rate
clock = pygame.time.Clock()
FPS = 60

# Animation states
SCENE_1 = "giving_udon"
SCENE_2 = "birthday_message"

class Animation:
    def __init__(self):
        self.current_scene = SCENE_1
        self.scene_timer = 0
        self.udon_hand_progress = 0
        self.speech_bubble_alpha = 0
        self.message_scale = 0
        self.heart_particles = []

    def update(self, dt):
        self.scene_timer += dt

        if self.current_scene == SCENE_1:
            # Animate udon bowl being handed over
            if self.scene_timer < 2.0:
                self.udon_hand_progress = min(1.0, self.scene_timer / 2.0)
            else:
                self.udon_hand_progress = 1.0

            # Fade in speech bubble
            if self.scene_timer > 1.5:
                self.speech_bubble_alpha = min(255, (self.scene_timer - 1.5) * 255)

            # Transition to next scene
            if self.scene_timer > 5.0:
                self.current_scene = SCENE_2
                self.scene_timer = 0

        elif self.current_scene == SCENE_2:
            # Scale up birthday message
            self.message_scale = min(1.2, self.scene_timer * 0.5)

            # Generate heart particles
            if self.scene_timer % 0.3 < 0.05:
                import random
                self.heart_particles.append({
                    'x': random.randint(100, 900),
                    'y': HEIGHT,
                    'speed': random.uniform(1.5, 3.0),
                    'size': random.randint(15, 30)
                })

            # Update heart particles
            for heart in self.heart_particles:
                heart['y'] -= heart['speed']

            # Remove off-screen hearts
            self.heart_particles = [h for h in self.heart_particles if h['y'] > -50]

def draw_willow_tree(surface, x, y):
    # Tree trunk
    pygame.draw.rect(surface, TREE_BROWN, (x - 25, y - 150, 50, 150))

    # Willow branches (drooping effect)
    for i in range(20):
        offset_x = (i - 10) * 20
        branch_x = x + offset_x
        # Draw curved branches
        points = []
        for j in range(15):
            curve_y = y - 150 + j * 10
            curve_x = branch_x + math.sin(j * 0.3) * 10
            points.append((curve_x, curve_y))
        if len(points) > 1:
            pygame.draw.lines(surface, WILLOW_GREEN, False, points, 3)

    # Main canopy
    pygame.draw.ellipse(surface, WILLOW_GREEN, (x - 150, y - 250, 300, 150))

def draw_person_boy(surface, x, y):
    # Head
    pygame.draw.circle(surface, SKIN_TONE_BOY, (x, y - 60), 25)

    # Brown hair
    pygame.draw.circle(surface, BROWN_HAIR, (x, y - 70), 25)
    pygame.draw.circle(surface, BROWN_HAIR, (x - 15, y - 65), 15)
    pygame.draw.circle(surface, BROWN_HAIR, (x + 15, y - 65), 15)

    # Face details
    pygame.draw.circle(surface, BLACK, (x - 8, y - 65), 2)  # Left eye
    pygame.draw.circle(surface, BLACK, (x + 8, y - 65), 2)  # Right eye
    pygame.draw.arc(surface, BLACK, (x - 8, y - 55, 16, 10), 3.14, 6.28, 2)  # Smile

    # Quarterzip (Navy blue)
    pygame.draw.rect(surface, NAVY_BLUE, (x - 30, y - 30, 60, 50))
    # Zipper detail
    pygame.draw.line(surface, WHITE, (x, y - 30), (x, y - 10), 2)

    # Khaki pants
    pygame.draw.rect(surface, KHAKI, (x - 30, y + 20, 25, 40))
    pygame.draw.rect(surface, KHAKI, (x + 5, y + 20, 25, 40))

def draw_person_girl(surface, x, y):
    # Head
    pygame.draw.circle(surface, SKIN_TONE_GIRL, (x, y - 60), 25)

    # Black hair (long)
    pygame.draw.circle(surface, BLACK, (x, y - 70), 25)
    pygame.draw.ellipse(surface, BLACK, (x - 30, y - 80, 60, 80))
    # Hair on shoulders
    pygame.draw.ellipse(surface, BLACK, (x - 40, y - 40, 30, 40))
    pygame.draw.ellipse(surface, BLACK, (x + 10, y - 40, 30, 40))

    # Face details
    pygame.draw.circle(surface, BLACK, (x - 8, y - 65), 2)  # Left eye
    pygame.draw.circle(surface, BLACK, (x + 8, y - 65), 2)  # Right eye
    pygame.draw.arc(surface, BLACK, (x - 10, y - 55, 20, 12), 3.14, 6.28, 2)  # Smile

    # White sundress
    pygame.draw.polygon(surface, WHITE, [
        (x - 35, y - 25),
        (x + 35, y - 25),
        (x + 45, y + 60),
        (x - 45, y + 60)
    ])
    # Straps
    pygame.draw.line(surface, WHITE, (x - 20, y - 30), (x - 15, y - 25), 4)
    pygame.draw.line(surface, WHITE, (x + 20, y - 30), (x + 15, y - 25), 4)

def draw_udon_bowl(surface, x, y, scale=1.0):
    bowl_width = int(60 * scale)
    bowl_height = int(40 * scale)

    # Bowl
    pygame.draw.ellipse(surface, UDON_BOWL, (x - bowl_width//2, y - bowl_height//2, bowl_width, bowl_height))
    # Broth
    pygame.draw.ellipse(surface, BROTH_COLOR, (x - bowl_width//2 + 5, y - bowl_height//2 + 5, bowl_width - 10, bowl_height - 15))
    # Noodles on top
    for i in range(5):
        offset = i * 6 - 12
        pygame.draw.arc(surface, NOODLE_COLOR, (x - 15 + offset, y - 10, 12, 8), 0, 3.14, 2)

def draw_speech_bubble(surface, x, y, text, alpha):
    font = pygame.font.Font(None, 28)
    text_surface = font.render(text, True, BLACK)

    # Create a surface with alpha
    bubble_surface = pygame.Surface((400, 80), pygame.SRCALPHA)

    # Bubble background
    pygame.draw.rect(bubble_surface, (255, 255, 255, alpha), (0, 0, 400, 60), border_radius=10)
    pygame.draw.polygon(bubble_surface, (255, 255, 255, alpha), [(50, 60), (70, 60), (60, 75)])
    pygame.draw.rect(bubble_surface, (0, 0, 0, alpha), (0, 0, 400, 60), 2, border_radius=10)

    # Text with alpha
    text_with_alpha = text_surface.copy()
    text_with_alpha.set_alpha(alpha)
    bubble_surface.blit(text_with_alpha, (20, 15))

    surface.blit(bubble_surface, (x - 200, y - 120))

def draw_heart(surface, x, y, size, color):
    # Simple heart shape
    pygame.draw.circle(surface, color, (int(x - size//4), int(y - size//4)), size//2)
    pygame.draw.circle(surface, color, (int(x + size//4), int(y - size//4)), size//2)
    pygame.draw.polygon(surface, color, [
        (x - size//2, y - size//4),
        (x, y + size//2),
        (x + size//2, y - size//4)
    ])

def draw_scene_1(surface, animation):
    # Background
    surface.fill(SKY_BLUE)

    # Grass
    pygame.draw.rect(surface, GRASS_GREEN, (0, HEIGHT - 150, WIDTH, 150))

    # Willow tree
    draw_willow_tree(surface, WIDTH // 2, HEIGHT - 150)

    # Boy (left side)
    boy_x = WIDTH // 2 - 120
    boy_y = HEIGHT - 90
    draw_person_boy(surface, boy_x, boy_y)

    # Girl (right side)
    girl_x = WIDTH // 2 + 120
    girl_y = HEIGHT - 90
    draw_person_girl(surface, girl_x, girl_y)

    # Udon bowl animation (moving from boy to girl)
    udon_start_x = boy_x + 40
    udon_end_x = girl_x - 40
    udon_x = udon_start_x + (udon_end_x - udon_start_x) * animation.udon_hand_progress
    udon_y = boy_y - 30 - abs(math.sin(animation.udon_hand_progress * 3.14)) * 20
    draw_udon_bowl(surface, int(udon_x), int(udon_y))

    # Speech bubble
    if animation.speech_bubble_alpha > 0:
        draw_speech_bubble(surface, WIDTH // 2, 150, "Happy Birthday, here is a bowl of udon.", animation.speech_bubble_alpha)

def draw_scene_2(surface, animation):
    # Gradient background
    for i in range(HEIGHT):
        color_ratio = i / HEIGHT
        r = int(255 * (1 - color_ratio) + 255 * color_ratio)
        g = int(182 * (1 - color_ratio) + 192 * color_ratio)
        b = int(193 * (1 - color_ratio) + 203 * color_ratio)
        pygame.draw.line(surface, (r, g, b), (0, i), (WIDTH, i))

    # Draw floating hearts
    for heart in animation.heart_particles:
        draw_heart(surface, heart['x'], heart['y'], heart['size'], PINK)

    # Birthday message
    font_large = pygame.font.Font(None, 80)
    font_medium = pygame.font.Font(None, 60)

    text1 = font_large.render("HAPPY 20th BIRTHDAY", True, (255, 20, 147))
    text2 = font_medium.render("BEAUTIFUL!", True, (255, 105, 180))

    # Apply scaling
    if animation.message_scale > 0:
        w1, h1 = text1.get_size()
        w2, h2 = text2.get_size()

        scaled_text1 = pygame.transform.scale(text1, (int(w1 * animation.message_scale), int(h1 * animation.message_scale)))
        scaled_text2 = pygame.transform.scale(text2, (int(w2 * animation.message_scale), int(h2 * animation.message_scale)))

        surface.blit(scaled_text1, (WIDTH // 2 - scaled_text1.get_width() // 2, HEIGHT // 2 - 80))
        surface.blit(scaled_text2, (WIDTH // 2 - scaled_text2.get_width() // 2, HEIGHT // 2 + 20))

def main():
    animation = Animation()
    running = True

    while running:
        dt = clock.tick(FPS) / 1000.0  # Delta time in seconds

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_r:
                    # Restart animation
                    animation = Animation()

        # Update animation
        animation.update(dt)

        # Draw current scene
        if animation.current_scene == SCENE_1:
            draw_scene_1(screen, animation)
        elif animation.current_scene == SCENE_2:
            draw_scene_2(screen, animation)

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
