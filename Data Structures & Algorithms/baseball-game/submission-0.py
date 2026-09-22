class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        # record
        # int -> add to stack
        # + -> add sum to record
        # - invalidate last action
        # D add product of the last 2 records
        for op in operations:    
            if op == "+":
                last_value = record[len(record) - 1]
                second_to_last_value = record[len(record) - 2]
                record.append(last_value + second_to_last_value)
            elif op == "C":     
                record.pop()
            elif op == "D":
                record.append(record[len(record) - 1] * 2)
            else:
                record.append(int(op))

        return sum(record)