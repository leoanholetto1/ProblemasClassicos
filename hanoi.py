from typing import TypeVar,Generic,List
T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self)->None:
        self._container: List[T] = []

    def push(selfself,item: T):
        selfself._container.append(item)

    def pop(self)->T:
        return self._container.pop()

    def __repr__(self)->str:
        return repr(self._container)

def hanoi(begin: Stack[int],end: Stack[int],temp: Stack[int],n:int)->None:
    if n==1:
        end.push(begin.pop())
    else:
        hanoi(begin,temp,end,n-1)
        hanoi(begin,end,temp,1)
        hanoi(temp,end,begin,n-1)

if __name__ == "__main__":
    num = int(input())
    tower_a: Stack[int] = Stack()
    tower_b: Stack[int] = Stack()
    tower_c: Stack[int] = Stack()
    for i in range(1,num+1):
        tower_a.push(i)
    hanoi(tower_a,tower_b,tower_c,num)
    print(tower_a)
    print(tower_b)
    print(tower_c)