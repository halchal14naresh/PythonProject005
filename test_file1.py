import os



class TestClass1:

    def test_method1(self):
        print("")
        print("********************** ")
        print("This is Test Method")
        print("This is Test Method 123")
        print("********************** ")
        print(" ")

        print("This is Just Test Method Do Code Change abcd")
        env_var = os.environ
        print(os.environ['sky'])
        print(os.environ['M3_HOME'])
        print(os.environ['nky'])
