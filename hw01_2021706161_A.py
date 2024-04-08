class ListNode: 
    """
    연결 리스트의 노드를 정의 각 노드는 'item'(해당 노드에 저장된 데이터)과 
    'next'(리스트에서 다음 노드를 가리키는 참조)를 속성으로 가짐.
    """
    def __init__(self, item, next=None):
        self.item = item # 노드가 저장할 데이터
        self.next = next # 다음 노드에 대한 참조

class LinkedListBasic:
    """
    각 linkedlist는 '__head'와(더미 에드 노드를 가리키는 참조) 
    '__numItems'(리스트에 있는 실제 데이터 노드의 수)를 가짐.
    여기서 사용된 더미 헤드 노드는 실제 데이터를 저장하진 않고,
    연결 리스트의 시작을 표시하는 용도로 사용됨.
    """
    def __init__(self):
        self.__head = ListNode('dummy') # 더미 노드 초기화
        self.__numItems = 0 # 리스트의 노드 개수 초기화

    def insert(self, i, newItem):
        """
        insert 메소드는 리스트의 특정 위치에 새 항목을 삽입함.
        위치는 0부터 시작.
        먼저 삽입할 위치의 이전 노드를 찾고(getNode 메소드 이용),
        새 노드를 생성하여 이전 노드와 다음 노드 사이에 연결하는 방식으로 이루어짐.
        """

        # 인덱스 유효성 검사
        if i < 0 or i > self.__numItems:
            return False  

        # 삽입 위치 찾기
        if i == 0:
            prevNode = self.__head
        else:
            prevNode = self.getNode(i - 1)
        
        # prevNode가 None이 아닌지 확인
        if prevNode is None:
            return False

        # 새 노드 생성 및 연결
        newNode = ListNode(newItem, prevNode.next)
        # 새 노드를 가리키도록 이전 노드 업데이트
        prevNode.next = newNode
        # 목록의 항목 수 늘리기
        self.__numItems += 1
        return True

    def getNode(self, i: int) -> ListNode:
        """
        getNode 메소드는 리스트에서 특정 위치의 노드를 찾아 반환함.
        주로 내부적으로 사용되며, 노드의 삽입이나 접근 시 필요.
        """

        # 인덱스 유효성 검사
        if i >= self.__numItems or i < 0:
            return None  

        curr = self.__head
        for index in range(i + 1):
            curr = curr.next
        return curr

def mergeAndSortLists(list1, list2):
    """
    mergeAndSortLists 함수는 두 연결 리스트를 인자로 받아, 
    그 두 리스트를 병합하고 정렬하여 새로운 리스트를 생성함.
    병합 과정은 두 리스트의 헤드부터 시작하여, 각 단계에서
    두 리스트의 현재 노드 중 더 작은 값을 가진 노드의 값을 새 리스트에 추가.
    이후 선택된 노드의 다음 노드로 이동하여 과정 반복.
    새로운 항목을 삽입할 위치를 찾는 과정은 선형 탐색을 사용.
    삽입할 항목보다 큰 첫 번째 항목의 위치를 찾음.
    """

    # 병합된 새 리스트 초기화
    mergedList = LinkedListBasic() 
    # 각 리스트의 시작 노드 가져오기
    current1, current2 = list1.getNode(0), list2.getNode(0)

    # 두 리스트 중 하나라도 아직 항목이 남아 있으면 계속 반복
    while current1 is not None and current1.item != 'dummy' or current2 is not None and current2.item != 'dummy':
        # current1과 current2 중에서 다음에 병합 리스트에 추가할 항목을 결정
        if current1 is None or current1.item == 'dummy' or (current2 is not None and current2.item != 'dummy' and current2.item < current1.item):
            item = current2.item
            current2 = current2.next
        else:
            item = current1.item
            current1 = current1.next

        # 병합 리스트에 항목 삽입
        position = 0 # 삽입 위치를 찾기 위해, position을 0부터 시작하여, 병합 리스트의 노드를 순회
        currentNode = mergedList.getNode(position)
        while currentNode and currentNode.item != 'dummy' and currentNode.item <= item:
            position += 1
            currentNode = mergedList.getNode(position)
        
        mergedList.insert(position, item)
    
    return mergedList

def populate_linked_list(linked_list, values):
    """
    연결 리스트와 값을 담은 리스트를 인자로 받아, 
    리스트의 값을 연결 리스트에 삽입.
    """
    for i, value in enumerate(values):
        linked_list.insert(i, value)

# LinkedListBasic의 인스턴스로 list1 및 list2 초기화
list1 = LinkedListBasic()
list2 = LinkedListBasic()

# list1과 list2를 각각의 값으로 채움
populate_linked_list(list1, [1, 1, 2, 5])
populate_linked_list(list2, [1, 2, 3, 4])

# list1과 list2 병합
mergedList = mergeAndSortLists(list1, list2)

# 최종 연결 리스트 프린트
def print_linked_list(linked_list):
    items = []
    current = linked_list.getNode(0)
    while current is not None and current.item != 'dummy':  # Adjusted condition
        items.append(current.item)
        current = current.next
    return items

# 최종 결괏값 프린트
print(print_linked_list(list1))
print(print_linked_list(list2))
print(print_linked_list(mergedList))
