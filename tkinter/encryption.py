from numpy import matrix


# PARAMETERS: these parameters specify matrix size and the required divisor for
# all input messages to have.
MAT_LEN = 5
ORD_GAP = 50
CONV_CT = 3

message = 'this is a test message'


# The first step of encryption is to read the text to be encrypted and ensure
# that it can be transformed into a (n x n) matrix where `n == MAT_LEN`.
def adjust_length(message):
    msg_length = len(message)
    remainder = MAT_LEN - (msg_length % MAT_LEN)
    return message + (' ' * remainder)


# The next step of encryption is to convert the text into numbers for matrix
# operations. The numericized text is then adjusted by the `ORD_GAP` amount.
def to_matrix(message):
    M1 = matrix([(ord(__) - ORD_GAP) for __ in message])
    M2 = M1.reshape((MAT_LEN, MAT_LEN))
    return M2


# The third step of encryption is to create the inverse matrix of
# the first matrix.
def to_inverse(input_matrix):
    return matrix(input_matrix).getI()

# The fourth step recovers the encrypted matrix and returns a password.
def recover(encrypted_matrix):
    inv_matrix = matrix(encrypted_matrix).getI()
    new_matrix = reduce(np.dot, [encrypted_matrix] + [inv_matrix] * CONV_CT)


def recover_test(A, B):
    AI = A.getI()
    return A.dot(B.getI())


message = to_matrix(adjust_length(message))
inv_msg = to_inverse(message)
# print('Message', message)
# reduced = reduce(matrix.dot, [inv_msg] * CONV_CT)
# print('Inverse', inv_msg.ravel())
# #print('Reduced', reduced.ravel())
# #print('Reduced-Back1', reduce(matrix.dot, [to_inverse(reduced)] * CONV_CT).ravel())
# print('Reduced-Back1', reduce(matrix.dot, [to_inverse(inv_msg)] * (CONV_CT-1)).ravel())

# print(to_inverse(inv_msg).dot(to_inverse(inv_msg)).dot(reduced))
# # print('Reduced-Back2', reduce(matrix.dot, [reduced] + [inv_msg] * CONV_CT).ravel())
# # print(inv_msg)
print(''.join([chr(int(__)) for __ in (to_inverse(inv_msg).ravel() + ORD_GAP).round().tolist()[0]]))
