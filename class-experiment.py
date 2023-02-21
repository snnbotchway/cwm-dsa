class A:
    a = "A"


class B:
    a = "B"


class C(B, A):
    # a = "C"
    pass


c = C()
print(c.a)
