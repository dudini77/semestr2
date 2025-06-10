import pygame
import sys
import random
import math
import os

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Shooter - Arcade Game")

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
HIGHLIGHT = (100, 200, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)

FONT = pygame.font.SysFont("arial", 36)
SMALL_FONT = pygame.font.SysFont("arial", 24)

menu_items = [
    "1. Start gry",
    "2. Zasady gry",
    "3. Najlepsze wyniki", 
    "4. O autorze",
    "5. Zakończenie programu"
]
selected_index = 0

class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - 60
        self.width = 40
        self.height = 30
        self.speed = 5
        self.bullets = []
    
    def update(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < SCREEN_WIDTH - self.width:
            self.x += self.speed
        if keys[pygame.K_UP] and self.y > 0:
            self.y -= self.speed
        if keys[pygame.K_DOWN] and self.y < SCREEN_HEIGHT - self.height:
            self.y += self.speed
    
    def shoot(self):
        bullet = {
            'x': self.x + self.width // 2 - 2,
            'y': self.y,
            'speed': 8
        }
        self.bullets.append(bullet)
    
    def update_bullets(self):
        self.bullets = [b for b in self.bullets if b['y'] > 0]
        for bullet in self.bullets:
            bullet['y'] = bullet['y'] - bullet['speed']
    
    def draw(self, screen):
        # Rysuj statek gracza
        pygame.draw.polygon(screen, GREEN, [
            (self.x + self.width//2, self.y),
            (self.x, self.y + self.height),
            (self.x + self.width, self.y + self.height)
        ])
        
        # Rysuj pociski
        for bullet in self.bullets:
            pygame.draw.rect(screen, YELLOW, (bullet['x'], bullet['y'], 4, 10))

class Enemy:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - 30)
        self.y = random.randint(-100, -30)
        self.width = 30
        self.height = 30
        self.speed = random.randint(4, 6)
        self.color = random.choice([RED, ORANGE, (255, 100, 100)])
    
    def update(self):
        self.y = self.y + self.speed
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, WHITE, (self.x, self.y, self.width, self.height), 2)



def start_game():
    
    pygame.mixer.music.load("muzyka/cosmic-serenity-238263.mp3")
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(-1)

    clock = pygame.time.Clock()
    running = True
    
    player = Player()
    enemies = []
    
    points = 0
    lives = 3
    enemy_spawn_timer = 0
    shoot_cooldown = 0
    
    stars = [(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)) for _ in range(50)]

    while running:
        dt = clock.tick(60)
        keys = pygame.key.get_pressed()
        
        # Obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_SPACE and shoot_cooldown <= 0:
                    player.shoot()
                    shoot_cooldown = 10
        
        if shoot_cooldown > 0:
            shoot_cooldown = shoot_cooldown - 1
        
        # Aktualizacja gracza
        player.update(keys)
        player.update_bullets()
        
        # Spawn wrogów
        enemy_spawn_timer = enemy_spawn_timer + 1
        if enemy_spawn_timer > 10: 
            enemies.append(Enemy())
            enemy_spawn_timer = 0
        
        # Aktualizacja wrogów
        for enemy in enemies[:]:
            enemy.update()
            if enemy.y > SCREEN_HEIGHT:
                enemies.remove(enemy)
        
        # Kolizje pociski vs wrogowie
        for bullet in player.bullets[:]:
            for enemy in enemies[:]:
                if (bullet['x'] < enemy.x + enemy.width and
                    bullet['x'] + 4 > enemy.x and
                    bullet['y'] < enemy.y + enemy.height and
                    bullet['y'] + 10 > enemy.y):
                    player.bullets.remove(bullet)
                    enemies.remove(enemy)
                    points = points + 10
                    break
        
        # Kolizje gracz vs wrogowie
        for enemy in enemies[:]:
            if (player.x < enemy.x + enemy.width and
                player.x + player.width > enemy.x and
                player.y < enemy.y + enemy.height and
                player.y + player.height > enemy.y):
                enemies.remove(enemy)
                lives = lives - 1
                if lives <= 0:
                    save_score(points)
                    show_game_over(points)
                    running = False
        
        # Rysowanie
        SCREEN.fill(BLACK)
        
        # Rysuj gwiazdy
        for star in stars:
            pygame.draw.circle(SCREEN, WHITE, star, 1)
        
        # Rysuj wszystkie obiekty
        player.draw(SCREEN)
        
        for enemy in enemies:
            enemy.draw(SCREEN)
        
        # HUD
        point_text = SMALL_FONT.render(f"Punkty: {points}", True, WHITE)
        life_text = SMALL_FONT.render(f"Życia: {lives}", True, WHITE)
        enemies_text = SMALL_FONT.render(f"Wrogowie: {len(enemies)}", True, WHITE)
        
        SCREEN.blit(point_text, (10, 10))
        SCREEN.blit(life_text, (10, 40))
        SCREEN.blit(enemies_text, (10, 70))
        
        # Instrukcje
        instructions = [
            "Strzałki - ruch",
            "SPACJA - strzał", 
            "ESC - menu"
        ]
        for i, inst in enumerate(instructions):
            inst_text = SMALL_FONT.render(inst, True, WHITE)
            SCREEN.blit(inst_text, (SCREEN_WIDTH - 150, 10 + i * 25))
        
        pygame.display.flip()

def save_score(score):
    """Zapisuje wynik do pliku"""
    try:
        scores = []
        if os.path.exists("scores.txt"):
            with open("scores.txt", "r", encoding="utf-8") as f:
                scores = [line.strip() for line in f.readlines() if line.strip()]
        
        scores.append(str(score))
        scores = sorted([int(s) for s in scores], reverse=True)[:10]
        
        with open("scores.txt", "w", encoding="utf-8") as f:
            for score in scores:
                f.write(f"{score}\n")
                
    except Exception as e:
        print(f"Błąd zapisu wyniku: {e}")

def show_game_over(final_score):
    """Pokazuje ekran końca gry"""
    SCREEN.fill(BLACK)
    
    game_over_text = FONT.render("KONIEC GRY!", True, RED)
    score_text = FONT.render(f"Twój wynik: {final_score}", True, WHITE)
    continue_text = SMALL_FONT.render("Naciśnij dowolny klawisz aby kontynuować", True, WHITE)
    
    SCREEN.blit(game_over_text, (SCREEN_WIDTH//2 - game_over_text.get_width()//2, 200))
    SCREEN.blit(score_text, (SCREEN_WIDTH//2 - score_text.get_width()//2, 250))
    SCREEN.blit(continue_text, (SCREEN_WIDTH//2 - continue_text.get_width()//2, 350))
    
    pygame.display.flip()
    
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

def draw_menu():
    SCREEN.fill(BLACK)
    
    # Tytul z efektem
    title_text = FONT.render("🚀 SPACE SHOOTER 🚀", True, HIGHLIGHT)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH//2, 80))
    SCREEN.blit(title_text, title_rect)
    
    for idx, item in enumerate(menu_items):
        color = HIGHLIGHT if idx == selected_index else WHITE
        text_surface = FONT.render(item, True, color)
        rect = text_surface.get_rect(center=(SCREEN_WIDTH//2, 150 + idx * 60))
        SCREEN.blit(text_surface, rect)
    
    nav_text = SMALL_FONT.render("Strzałki + ENTER", True, WHITE)
    nav_rect = nav_text.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT - 50))
    SCREEN.blit(nav_text, nav_rect)
    
    pygame.display.flip()

def show_text_screen(lines):
    SCREEN.fill(BLACK)
    
    for i, line in enumerate(lines):
        text_surface = SMALL_FONT.render(line, True, WHITE)
        SCREEN.blit(text_surface, (50, 100 + i * 30))
    
    exit_text = SMALL_FONT.render("Naciśnij dowolny klawisz aby wrócić", True, HIGHLIGHT)
    SCREEN.blit(exit_text, (50, SCREEN_HEIGHT - 50))
    
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False

def show_rules():
    rules = [
        "🎮 ZASADY GRY - SPACE SHOOTER:",
        "",
        "🎯 CEL:",
        "- Strzelaj do wrogów i zdobywaj punkty",
        "- Unikaj kolizji z wrogami",
        "",
        "🕹️ STEROWANIE:",
        "- Strzałki - poruszanie statkiem",
        "- SPACJA - strzelanie",
        "- ESC - powrót do menu",
        "",
        "💎 WROGOWIE:",
        "- Czerwone kwadraty spadają z góry",
        "- Każdy zniszczony wróg = +10 punktów",
        "- Kolizja z wrogiem = utrata życia",
        "",
        "⚡ PUNKTACJA:",
        "- Za każdego zniszczonego wroga: +10 punktów"
    ]
    show_text_screen(rules)

def show_high_scores():
    try:
        scores_lines = ["🏆 NAJLEPSZE WYNIKI:", ""]
        
        if os.path.exists("scores.txt"):
            with open("scores.txt", "r", encoding="utf-8") as f:
                scores = [line.strip() for line in f.readlines() if line.strip()]
                
            if scores:
                for i, score in enumerate(scores[:10], 1):
                    medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else "🏅"
                    scores_lines.append(f"{medal} {i}. {score} punktów")
            else:
                scores_lines.append("Brak wyników - zagraj pierwszą grę!")
        else:
            scores_lines.append("Brak pliku z wynikami")
            
    except Exception as e:
        scores_lines = ["🏆 NAJLEPSZE WYNIKI:", "", f"Błąd odczytu: {str(e)}"]

    show_text_screen(scores_lines)

def show_about():
    about = [
        "👨‍💻 O AUTORZE:",
        "",
        "Autor: Mateusz Dudek"
    ]
    show_text_screen(about)

def handle_selection(index):
    if index == 0:
        start_game()
    elif index == 1:
        show_rules()
    elif index == 2:
        show_high_scores()
    elif index == 3:
        show_about()
    elif index == 4:
        pygame.quit()
        sys.exit()

def main():
    global selected_index
    clock = pygame.time.Clock()

    while True:
        draw_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_index = (selected_index - 1) % len(menu_items)
                elif event.key == pygame.K_DOWN:
                    selected_index = (selected_index + 1) % len(menu_items)
                elif event.key == pygame.K_RETURN:
                    handle_selection(selected_index)

        clock.tick(60)

if __name__ == "__main__":
    main()