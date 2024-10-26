from random import randint


def set_enemy_health() -> int:
    return randint(80, 120)


def get_lite_attack() -> int:
    return randint(2, 5)


def get_mid_attack() -> int:
    return randint(15, 25)


def get_hard_attack() -> int:
    return randint(30, 40)


def compare_valumes(enemy_health, user_total_attack) -> bool:
    point_difference: int = abs(enemy_health - user_total_attack)
    if 0 <= point_difference <= 10:
        return True
    
    return False


def get_user_attack() -> int:
    total: int = 0
    sum_attack_value: int = 0
    attacks_types = {
        'lite': get_lite_attack,
        'mid': get_mid_attack,
        'hard': get_hard_attack,
    }

    for i in range(5):
        input_attack: str = input('Введи тип атаки: ').lower()
        attack_value: int = attacks_types[input_attack]()
        print(f'Количество очков твоей атаки: {attack_value}.')
        total += 1
        sum_attack_value += attack_value
    
    return sum_attack_value


def run_game():
    user_total_attack: int = get_user_attack()
    enemy_health: int = set_enemy_health()
    print(f'Тобой нанесён урон противнику равный {user_total_attack}.')
    print(f'Очки здоровья противника до твоей атаки: {enemy_health}.')
    if compare_valumes(enemy_health, user_total_attack):
        print('Ура! Победа за тобой!')
    else:
        print('В этот раз не повезло :( Бой проигран.')
    
    yes_no = {
        'Y': True,
        'N': False,
        'y': True,
        'n': False,
    }

    replay: str = input('Чтобы сыграть ещё раз, введи "y"; '
                   'если не хочешь продолжать игру, введи "n": ')
    if replay not in yes_no:
        raise ValueError('Такой команды в игре нет.')
    
    return yes_no[replay]
