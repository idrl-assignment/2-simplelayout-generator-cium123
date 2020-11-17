from simplelayout.cli import get_options
import scipy.io
import scipy
from simplelayout.generator import generate_matrix, save_matrix, save_fig


def main():
    args = get_options()
    matrix = generate_matrix(args.board_grid, args.unit_grid, args.unit_n, args.positions)
    mdict = {"matrix": matrix}
    scipy.io.savemat("file_name.mat", mdict)
    scipy.misc.imsave("file_name.jpg", matrix)


if __name__ == "__main__":
    main()
