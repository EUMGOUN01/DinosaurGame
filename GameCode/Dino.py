import pygame

# Pygame 초기화
pygame.init()

# 화면 크기 설정
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("크롬 공룡 게임")  # 윈도우 제목을 한글로 설정

# 색상 정의
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# 공룡 설정
dino_width, dino_height = 50, 50
dino_x, dino_y = 50, HEIGHT - dino_height
is_jumping = False
jump_velocity = 15
gravity = 1

# 장애물 설정
obstacle_width, obstacle_height = 20, 40
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height
obstacle_velocity = 10

# 시작 화면 설정
start_font = pygame.font.SysFont('malgungothic', 50)
start_text = start_font.render("Jump! Dinosaur", True, BLACK)
instruction_font = pygame.font.SysFont('malgungothic', 20)
instruction_text = instruction_font.render("Press SPACE to start", True, BLACK)

# 게임 오버 화면 설정
game_over_font = pygame.font.SysFont('malgungothic', 50)
game_over_text = game_over_font.render("GAME OVER", True, BLACK)
restart_text = instruction_font.render("Press 'R' to restart", True, BLACK)

# 게임 클리어 화면 설정
game_clear_font = pygame.font.SysFont('malgungothic', 50)
game_clear_text = game_clear_font.render("GAME CLEAR", True, BLACK)

# 점수 설정
score = 0
score_font = pygame.font.SysFont('malgungothic', 30)

# 게임 상태 변수
is_start_screen = True
is_game_over = False
is_game_clear = False
running = True
clock = pygame.time.Clock()

# 점수 증가 관련 변수
score_increment = 1
score_increment_interval = 3  # 장애물을 통과할 때마다 점수가 증가하는 간격 (프레임 단위)
score_increment_timer = 0

# 깜빡임 변수
blink_timer = 0
blink_interval = 500  # 깜빡임 간격 (밀리초 단위)
show_instruction = True  # 깜빡임 상태 변수

# 게임 재시작 문구를 위한 깜빡임 변수
restart_blink_timer = 0
restart_blink_interval = 500  # 깜빡임 간격 (밀리초 단위)
show_restart_instruction = True  # 깜빡임 상태 변수

while running:
    if is_start_screen:
        screen.fill(WHITE)  # 시작 화면 배경을 흰색으로 채우기
        screen.blit(start_text, (WIDTH // 2 - start_text.get_width() // 2, HEIGHT // 2 - start_text.get_height() // 2))
        
        # 깜빡이는 문구 처리
        current_time = pygame.time.get_ticks()
        if current_time - blink_timer > blink_interval:
            blink_timer = current_time
            show_instruction = not show_instruction  # 상태를 반전하여 깜빡이도록 함
        
        if show_instruction:
            screen.blit(instruction_text, (WIDTH // 2 - instruction_text.get_width() // 2, HEIGHT // 2 + start_text.get_height() // 2 + 10))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # 창 닫기 이벤트 처리
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_start_screen = False  # 스페이스 바를 누르면 시작 화면을 빠져나가 메인 게임으로 진입
    
    elif is_game_over:
        screen.fill(WHITE)  # 게임 오버 화면 배경을 흰색으로 채우기
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
        
        # 깜빡이는 문구 처리
        current_time = pygame.time.get_ticks()
        if current_time - restart_blink_timer > restart_blink_interval:
            restart_blink_timer = current_time
            show_restart_instruction = not show_restart_instruction  # 상태를 반전하여 깜빡이도록 함
        
        if show_restart_instruction:
            screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + game_over_text.get_height() // 2 + 10))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # 창 닫기 이벤트 처리
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    is_game_over = False
                    is_start_screen = True
                    score = 0  # 점수 초기화
                    # 게임 재시작을 위한 변수 초기화
                    dino_y = HEIGHT - dino_height
                    obstacle_x = WIDTH
                    obstacle_velocity = 10
                    is_jumping = False
    
    elif is_game_clear:
        screen.fill(WHITE)  # 게임 클리어 화면 배경을 흰색으로 채우기
        screen.blit(game_clear_text, (WIDTH // 2 - game_clear_text.get_width() // 2, HEIGHT // 2 - game_clear_text.get_height() // 2))
        
        # 깜빡이는 문구 처리
        current_time = pygame.time.get_ticks()
        if current_time - restart_blink_timer > restart_blink_interval:
            restart_blink_timer = current_time
            show_restart_instruction = not show_restart_instruction  # 상태를 반전하여 깜빡이도록 함
        
        if show_restart_instruction:
            screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT // 2 + game_clear_text.get_height() // 2 + 10))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # 창 닫기 이벤트 처리
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    is_game_clear = False
                    is_start_screen = True
                    score = 0  # 점수 초기화
                    # 게임 재시작을 위한 변수 초기화
                    dino_y = HEIGHT - dino_height
                    obstacle_x = WIDTH
                    obstacle_velocity = 10
                    is_jumping = False
    
    else:
        screen.fill(WHITE)  # 메인 게임 화면 배경을 흰색으로 채우기
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False  # 창 닫기 이벤트 처리
        
        # 점수 증가 로직
        score_increment_timer += 1
        if score_increment_timer >= score_increment_interval:
            score += score_increment
            score_increment_timer = 0
        
        # 공룡 점프 로직
        keys = pygame.key.get_pressed()
        if not is_jumping:
            if keys[pygame.K_SPACE]:  # 스페이스 키를 누르면 점프 시작
                is_jumping = True
                initial_jump_velocity = jump_velocity
        
        if is_jumping:
            dino_y -= initial_jump_velocity  # 공룡을 위로 이동
            initial_jump_velocity -= gravity  # 점프 속도에 중력 적용
            if initial_jump_velocity < -jump_velocity:
                is_jumping = False
                dino_y = HEIGHT - dino_height  # 공룡을 바닥으로 리셋
        
        # 장애물 이동 로직
        obstacle_x -= obstacle_velocity
        if obstacle_x < 0:
            obstacle_x = WIDTH  # 장애물이 화면 밖으로 나가면 위치 초기화
            obstacle_velocity += 0.5  # 게임 난이도 증가: 속도 증가
        
        # 충돌 감지
        if dino_x < obstacle_x < dino_x + dino_width and dino_y + dino_height > obstacle_y:
            is_game_over = True  # 충돌 시 게임 오버 화면으로 전환
        
        # 점수 표시
        score_text = score_font.render(f"SCORE {score:04d}", True, BLACK)
        screen.blit(score_text, (WIDTH - score_text.get_width() - 10, 10))
        
        # 공룡 그리기
        pygame.draw.rect(screen, BLACK, (dino_x, dino_y, dino_width, dino_height))
        
        # 장애물 그리기
        pygame.draw.rect(screen, RED, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
        
        # 게임 클리어 조건
        if score >= 1000:
            is_game_clear = True
    
    pygame.display.update()  # 화면 업데이트
    clock.tick(30)  # 초당 30 프레임으로 설정

pygame.quit()  # Pygame 종료