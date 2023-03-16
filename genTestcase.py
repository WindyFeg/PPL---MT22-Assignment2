with open("test_cases.txt", "w") as f:
    for i in range(1, 101):
        test_name = f"test_{i}"
        input_str = '""""""'
        expect_str = '""""""'
        test_str = f"def {test_name}(self):\n    input = {input_str}\n    expect = {expect_str}\n    self.assertTrue(TestAST.test(input, expect, {300 + i}))\n\n"
        f.write(test_str)
