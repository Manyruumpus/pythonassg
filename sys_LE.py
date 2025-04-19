import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
#  install spicy and sparse first 
def solve_linear_system(A_input, b_input, use_iter=False, tol=1e-8):
    #  to solve Ax = b using direct or iterative (CG) method
    # first make sure inputs are in usable form
    if sp.issparse(A_input):
        A = A_input
    else:
        A = np.array(A_input)

    b = np.array(b_input, dtype=float).flatten() 

    # Sanity checks
    if A.shape[0] != A.shape[1]:
        raise ValueError("Matrix A needs to be square.")
    
    if b.shape[0] != A.shape[0]:
        raise ValueError("Length of b doesn't match A's dimensions.")

    # Decide between direct or CG solve
    if not use_iter or not sp.issparse(A):
        try:
            return np.linalg.solve(A, b)  # plain ol' direct method
        except np.linalg.LinAlgError:
            raise ValueError("Direct solve failed — maybe A is singular?")
    else:
        #  using Conjugate Gradient method
        if not sp.issparse(A):
            A = sp.csr_matrix(A)  # convert to CSR format if needed

        # CG method expects a tolerance — using rtol here 
        x, status = spla.cg(A, b, rtol=tol)

        if status != 0:
            #  status > 0 means no convergence, < 0 means illegal input
            raise ValueError(f"CG method didn't converge (status code: {status})")

        return x


# Tests 
if __name__ == "__main__":
    # Basic small system (dense)
    A1 = np.array([[4, 1],
                   [1, 3]])
    b1 = np.array([1, 2])

    print("Trying small dense system...")
    try:
        x1 = solve_linear_system(A1, b1)
        print("Solution x:", x1)
    except ValueError as err:
        print("Error in dense solve:", err)

    # Now testing sparse solve with a big matrix
    print("\nSolving a large sparse system (1000 x 1000)...")

    N = 1000
    main_diag = 2 * np.ones(N)
    side_diag = -1 * np.ones(N - 1)

    # Create tridiagonal sparse matrix
    A_sparse = sp.diags([side_diag, main_diag, side_diag], offsets=[-1, 0, 1])
    b_sparse = np.ones(N)

    try:
        x2 = solve_linear_system(A_sparse, b_sparse, use_iter=True, tol=1e-6)
        print("First 5 values of solution:", x2[:5])  # No need to print it all
    except ValueError as e:
        print("Sparse solver failed:", e)
