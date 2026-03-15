# # Bitwise operators are used to perform bitwise operations on integers.
# # Bitwise operators include:
# & 	AND	Sets each bit to 1 if both bits are 1	x & y	
# |	OR	Sets each bit to 1 if one of two bits is 1	x | y	
# ^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
# ~	NOT	Inverts all the bits	~x	
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2	
# Example of bitwise operators
a = 5  # In binary: 0101
b = 3  # In binary: 0011
print(a & b)  # Output: 1 (In binary: 0001)
print(a | b)  # Output: 7 (In binary: 0111)
print(a ^ b)  # Output: 6 (In binary: 0110)
print(~a)  # Output: -6 (In binary: ...11111010)
print(a << 1)  # Output: 10 (In binary: 1010)
print(a >> 1)  # Output: 2 (In binary: 0010)