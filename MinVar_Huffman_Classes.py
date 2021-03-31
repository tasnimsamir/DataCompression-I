
import heapq
class HeapNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    # defining comparators less_than and equals
    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        if(other == None):
            return False
        if(not isinstance(other, HeapNode)):
            return False
        return self.freq == other.freq



class MinVar_huaffman:
    def __init__(self):
        self.heap = []
        self.minVar_codes = {}
        self.reverse_mapping = {}

    def make_heap(self,extended_dict):
        for key in extended_dict:
            node = HeapNode(key, extended_dict[key])
            heapq.heappush(self.heap, node)

    def merge_nodes(self):
        while (len(self.heap) > 1):
            node1 = heapq.heappop(self.heap)
            node2 = heapq.heappop(self.heap)

            merged = HeapNode(None, node1.freq + node2.freq)
            merged.left = node1
            merged.right = node2

            heapq.heappush(self.heap, merged)

    def make_codes_helper(self,root, current_code):
        if (root == None):
            return
        if (root.char != None):
            self.minVar_codes[root.char] = current_code
            self.reverse_mapping[current_code] = root.char
            return
        self.make_codes_helper(root.left, current_code + "0")
        self.make_codes_helper(root.right, current_code + "1")

    def make_codes(self):
        root = heapq.heappop(self.heap)
        current_code = ""
        self.make_codes_helper(root, current_code)

    def get_extended_encoded_text(self,text,string_length):
        encoded_text = ""
        extended_text_len = int(string_length / 2)
        for i in range(0, extended_text_len, 2):
            encoded_text += self.minVar_codes[text[i] + text[i + 1]]
        return encoded_text
    def Code_dict(self,extended_dict):
        self.make_heap(extended_dict)
        self.merge_nodes()
        self.make_codes()
        return self.minVar_codes