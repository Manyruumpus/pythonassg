import numpy as np

try:
    import scipy.sparse as sparse
    import scipy.sparse.linalg as splinalg
except ImportError:
    sparse = None
    splinalg = None

def solve_system(A, b, use_iterative=False, tolerance=1e-8):
    # Solves Ax = b using either direct method or CG (if sparse & asked).
    A = np.array(A) if sparse is None or not sparse.issparse(A) else A
    b = np.array(b, dtype=float).flatten()

    n = A.shape[0]
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix A must be square.")
    if b.shape[0] != n:
        raise ValueError("Vector b must match A in dimensions.")

    if not use_iterative or sparse is None or not sparse.issparse(A):
        try:
            return np.linalg.solve(A, b)
        except np.linalg.LinAlgError:
            raise ValueError("Direct solver failed. Check if A is singular.")
    else:
        A_sparse = A if sparse.issparse(A) else sparse.csr_matrix(A)
        x, info = splinalg.cg(A_sparse, b, tol=tolerance)
        if info != 0:
            raise ValueError("Conjugate Gradient failed to converge.")
        return x

# Test example
if __name__ == "__main__":
    A1 = np.array([[4, 1], [1, 3]])
    b1 = np.array([1, 2])
    x1 = solve_system(A1, b1)
    print("Solution (direct):", x1)

    if sparse is not None:
        # basic sparse system
        size = 1000
        main_diag = 2 * np.ones(size)
        side_diag = -1 * np.ones(size - 1)
        A_sparse = sparse.diags([side_diag, main_diag, side_diag], [-1, 0, 1])
        b_sparse = np.ones(size)

        x2 = solve_system(A_sparse, b_sparse, use_iterative=True, tolerance=1e-6)
        print("First few entries of sparse solution:", x2[:5])
