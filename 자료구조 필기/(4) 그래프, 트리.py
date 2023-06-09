# 그래프 자료구조
"""정점(Node)과 간선(Edge)으로 이루어진 자료 구조"""
"""
무방향 그래프(=양방향 그래프), 방향 그래프

순환 그래프(Cyclic Graph), 비순환 그래프(Acyclic Graph)
사이클이 하나라도 존재하면 순환 그래프이다

DAG(Directional Acyclic Graph): 방향성 비순환 그래프
예: VCS(Version Control System)
"""
# 연결 요소(Connected Componen)
"""
다른 연결 요소와 서로 연결되어 있지 않은 하나의 묶음 단위
"""

# 트리
"""순환성이 없는 무방향 그래프"""
"""
루트 노드(root node): 어떠한 노드든지 루트 정점이 될 수 있다

리프 노드(leaf node): 간선이 하나뿐인 노드(루트 노드 기준 가장 바깥쪽 노드)

특징
- (노드 개수) = (간선 개수) + 1
- 한 노드에서 다른 노드로 가는 경로는 반드시 존재하며 유일하다
"""

# 자료구조에서의 트리
"""
노드끼리 부모->자식 관계가 존재하는 방향 그래프이다.
root는 하나이다.
"""

# 트리의 구현
"""라이브러리에 없으므로 직접 구현해야 함"""

# 방법1. 인접행렬
"""
n x n 이차원배열을 선언하고, 간선이 존재하면 1, 존재하지 않으면 0으로 간선 정보 표현
그래프 정보를 간선으로만 나타낼 수 있음

특징 
- [k][k]번째 인덱스는 반드시 0 (자기 자신에게 이어지는 간선은 존재 불가)
- 대각선 기준 대칭이 됨
"""

# 방법2. 인접리스트
"""
Linked List를 사용하여 표현

특징
- 간선이 존재하는 영역에만 공간이 할당
"""

# 인접행렬 vs 인접리스트
"""
두 방식의 장단점을 비교

메모리 사용량: 인접행렬 > 인접리스트
소요 시간: 인접행렬 < 인접리스트
(시간, 공간은 trade-off 관계에 있기 떄문)

ex) 정점이 최대 N 개, 간선 개수가 N^2 개일 때 -> 인접행렬 사용
ex) 정점이 최대 N개, 간선 개수가 2N 개일 때 -> 인접리스트 사용
"""