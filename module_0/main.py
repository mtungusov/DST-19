import numpy as np

def score_game(game_core, predict_func):
  '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
  count_ls = []
  np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
  random_array = np.random.randint(1,101, size=(1000))
  for number in random_array:
    count_ls.append(game_core(number, predict_func))
  score = int(np.mean(count_ls))
  print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
  return(score)


def game_core(number, predict_func):
  '''Угадываем число, сокращая диапазон для угадывания'''
  r_min = 1
  r_max = 100
  count = 1
  predict = np.random.randint(r_min, r_max + 1)
  
  while predict != number:
    count += 1
    if number > predict:
      r_min = predict + 1
      predict = predict_func(r_min, r_max)
    else:
      r_max = predict - 1
      predict = predict_func(r_min, r_max)
  
  return(count)


def gen_predict_v1(r_min, r_max):
  '''Угадываем число через случайную функцию'''
  return np.random.randint(r_min, r_max+1)


def gen_predict_v2(r_min, r_max):
  '''Угадываем число бинарным способом'''
  return (r_max + r_min) // 2


# Запускаем программу
print('Угадываем случайно:')
score_game(game_core, gen_predict_v1)

print()

print('Угадываем бинарно:')
score_game(game_core, gen_predict_v2)
