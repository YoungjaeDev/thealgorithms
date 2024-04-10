def solution(k, dungeons):
  if len(dungeons) == 0:
    return 0

  if all(not isinstance(item, list) for item in dungeons):
    dungeons = [dungeons]

  answer = 0
  dungeons_length = len(dungeons)
  hp = k

  for i in range(dungeons_length):
    min_hp = dungeons[i][0]
    if hp >= min_hp:
      res = solution(hp - dungeons[i][1], dungeons[:i] + dungeons[i + 1:])
      if res >= 0:
        answer = max(answer, res + 1)

  return answer


if __name__ == "__main__":
  k = 80
  dungeons = [[80, 20], [50, 40], [30, 10]]
  answer = solution(k, dungeons)

  assert answer == 3
  print('end')
