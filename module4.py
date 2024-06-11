"""MSCS2202 - Assignment 4.2"""

def main():
  n = int(input('Please provide a positive integer N: '))

  print(f'Please provide {n} integers line by line:')
  inputs = []
  for _ in range(n):
    inputs.append(int(input()))

  x = int(input('Please provide an integer X: '))
  for i in range(n):
    if inputs[i] == x:
      print(i+1)
      return
  print(-1)


if __name__ == '__main__':
    main()
