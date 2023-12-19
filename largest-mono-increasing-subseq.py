class Lis:
    nums = []
    Lis = []
    length_lis = 0

    sub_len = []
    sub_seq = []

    def __init__(self, nums):
        self.nums = nums

    def longest_increasing_subsequence(self):
        N = len(self.nums)
        self.sub_seq = [0] * N
        self.sub_len = [-1] * (N + 1)
        self.sub_len[0] = -1
        self.length_lis = 0

        for i in range(N):
            lo = 1
            hi = self.length_lis + 1

            while lo < hi:
                mid = lo + (hi - lo) // 2

                if self.nums[self.sub_len[mid]] >= self.nums[i]:
                    hi = mid
                else:
                    lo = mid + 1

            newL = lo
            self.sub_seq[i] = self.sub_len[newL - 1]
            self.sub_len[newL] = i

            if newL > self.length_lis:
                self.length_lis = newL

        self.Lis = [0] * self.length_lis
        k = self.sub_len[self.length_lis]
        for j in range(self.length_lis - 1, -1, -1):
            self.Lis[j] = self.nums[k]
            k = self.sub_seq[k]

        return self.Lis

    def print_lis(self):
        print("LIS: ", self.Lis)

    def print_length_lis(self):
        print("Length of LIS: ", self.length_lis)

    def get_lis(self):
        return self.Lis

    def get_length_lis(self):
        return self.length_lis


if __name__ == "__main__":
    nums = [4, 1, 13, 7, 0, 2, 8, 11, 3, 13, 4, 5]
    Lis = Lis(nums)
    Lis.longest_increasing_subsequence()
    Lis.print_lis()
    Lis.print_length_lis()
