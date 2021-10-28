from typing import List

# recursive_dfs
def canVisitAllRooms(rooms: List[List[int]]) -> bool:        
    def recursive_dfs(idx):        
        seen.add(idx)
        keys = rooms[idx]
        for key in keys:
            if key not in seen:
                recursive_dfs(key)        
    seen = set()                
    recursive_dfs(0)
    if len(rooms) == len(seen):
        return True
    else:
        return False


# iterative_dfs
def canVisitAllRooms(rooms: List[List[int]]) -> bool:
        seen = set()
        stack = []
        seen.add(0)
        stack.append(0)
        
        while stack:
            room_idx = stack.pop()
            for key in rooms[room_idx]:
                if key not in seen:
                    stack.append(key)
                    seen.add(key)
        
        if len(rooms) == len(seen):
            return True
        else:
            return False