# this code will count till the number you have provided.

def count(n):
  for i in range(1,n+1):
    print(i)
    
if __name__ == "__main__":
  print("Give a number: ",end="")
  i = int(input())
  count(i)
