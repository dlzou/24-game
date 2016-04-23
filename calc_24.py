count = 0
solutions = []

def calculate(nums, exps, n):
    if n == 1:
        if abs(nums[0] - 24) <= 0.000001:
            exps[0] = exps[0][1:-1]
            global solutions
            if exps[0] not in solutions:
                print(exps[0])
                global count
                count += 1
                solutions.append(exps[0])

    i = 0; j = i + 1
    while i < n:
        while j < n:
            num_a = nums[i]
            num_b = nums[j]
            nums[j] = nums[n - 1]

            exp_a = exps[i]
            exp_b = exps[j]
            exps[j] = exps[n - 1]

            # print(str(i) + ' ' + str(j)) #test

            exps[i] = "({}+{})".format(exp_a, exp_b)
            nums[i] = num_a + num_b
            calculate(nums, exps, n - 1)

            exps[i] = "({}-{})".format(exp_a, exp_b)
            nums[i] = num_a - num_b
            calculate(nums, exps, n - 1)
            exps[i] = "({}-{})".format(exp_b, exp_a)
            nums[i] = num_b - num_a
            calculate(nums, exps, n - 1)

            exps[i] = "({}*{})".format(exp_a, exp_b)
            nums[i] = num_a * num_b
            calculate(nums, exps, n - 1)

            if num_b != 0:
                exps[i] = "({}/{})".format(exp_a, exp_b)
                nums[i] = num_a / num_b
                calculate(nums, exps, n - 1)
            if num_a != 0:
                exps[i] = "({}/{})".format(exp_b, exp_a)
                nums[i] = num_b / num_a
                calculate(nums, exps, n - 1)

            nums[i] = num_a
            nums[j] = num_b
            exps[i] = exp_a
            exps[j] = exp_b

            j += 1
        i += 1

def reset():
    global count
    count = 0
    global solutions
    solutions[:] = []
