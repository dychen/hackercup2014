import java.io.BufferedReader;
import java.io.FileReader;
import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Queue;
import java.util.LinkedList;
import java.lang.Math;

public class AAAAAA{

    private class Block {
        private int row, col, prevdir;
        private Block(int r, int c, int pd) {
            row = r;
            col = c;
            prevdir = pd;
        }
    }

    public int longest_path(int[][] mat, int[][] mat2, int[][] mat3, int rows, int cols) {
        int r, c, prevdir;
        int maxlen = -1;
        Queue<Block> q = new LinkedList<Block>();
        Queue<Block> q2 = new LinkedList<Block>();
        Queue<Block> q3 = new LinkedList<Block>();
        Block b;
        b = new Block(1, 1, 1);
        b = new Block(2, 2, 2);
        q.add(new Block(0, 0, -1));
        mat[0][0] = 1;
        while (q.peek() != null) {
            b = q.remove();
            r = b.row;
            c = b.col;
            prevdir = b.prevdir;
            if (r+1 < rows && mat[r+1][c] >= 0) {       
                if (mat[r][c] + 1 > mat[r+1][c]) {
                    mat[r+1][c] = mat[r][c] + 1;
                    q.add(new Block(r+1, c, 0));
                }
            }
            if (c+1 < cols && mat[r][c+1] >= 0) {
                if (mat[r][c] + 1 > mat[r][c+1]) {
                    mat[r][c+1] = mat[r][c] + 1;
                    q.add(new Block(r, c+1, 1));
                }
            }
            if (r-1 >= 0 && mat[r-1][c] >= 0 && prevdir != 0) {
                if (r+1 == rows || mat[r+1][c] < 0) {
                    mat2[r-1][c] = Math.max(mat[r-1][c], mat[r][c] + 1);
                    q2.add(new Block(r-1, c, 2));
                }
            }
            if (c-1 >= 0 && mat[r][c-1] >= 0 && prevdir != 1) {
                if (c+1 == cols || mat[r][c+1] < 0) {
                    mat2[r][c-1] = Math.max(mat[r][c-1], mat[r][c] + 1);
                    q2.add(new Block(r, c-1, 3));
                }
            }

        }
        while (q2.peek() != null) {
            b = q2.remove();
            r = b.row;
            c = b.col;
            prevdir = b.prevdir;
            if (r-1 >= 0 && mat2[r-1][c] >= 0 && prevdir == 2) {
                mat2[r-1][c] = Math.max(mat2[r-1][c], mat2[r][c] + 1);
                q2.add(new Block(r-1, c, 2));
            }
            if (c-1 >= 0 && mat2[r][c-1] >= 0 && prevdir == 3) {
                mat2[r][c-1] = Math.max(mat2[r][c-1], mat2[r][c] + 1);
                q2.add(new Block(r, c-1, 3));
            }
            if (r+1 < rows && mat2[r+1][c] >= 0 && prevdir != 2) {
                mat3[r+1][c] = Math.max(mat2[r+1][c], mat2[r][c] + 1);
                q3.add(new Block(r+1, c, 0));
            }
            if (c+1 < cols && mat2[r][c+1] >= 0 && prevdir != 3) {
                mat3[r][c+1] = Math.max(mat2[r][c+1], mat2[r][c] + 1);
                q3.add(new Block(r, c+1, 1));
            }
        }
        while (q3.peek() != null) {
            b = q3.remove();
            r = b.row;
            c = b.col;
            prevdir = b.prevdir;
            if (r+1 < rows && mat3[r+1][c] >= 0 && prevdir != 2) {
                if (mat3[r][c] + 1 > mat3[r+1][c]) {
                    mat3[r+1][c] = Math.max(mat3[r+1][c], mat3[r][c] + 1);
                    q3.add(new Block(r+1, c, 0));
                }
            }
            if (c+1 < cols && mat3[r][c+1] >= 0 && prevdir != 3) {
                if (mat3[r][c] + 1 > mat3[r][c+1]) {
                    mat3[r][c+1] = Math.max(mat3[r][c+1], mat3[r][c] + 1);
                    q3.add(new Block(r, c+1, 1));
                }
            }

        }
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (mat[i][j] > maxlen)
                    maxlen = mat[i][j];
                if (mat2[i][j] > maxlen)
                    maxlen = mat2[i][j];
                if (mat3[i][j] > maxlen)
                    maxlen = mat3[i][j];
            }
        }
        return maxlen;
    }

    public static void main(String args[]) {
        try {
            //String FILENAME = "aaaaaa_example_input.txt";
            String FILENAME = "aaaaaa.txt";
            String OUTPUT = "aaaaaa_output.txt";
            BufferedReader reader = new BufferedReader(new FileReader(FILENAME));
            BufferedWriter writer = new BufferedWriter(new FileWriter(OUTPUT));
            String line;
            String[] dims;
            int rows;
            int cols;
            int NUM_INPUT = Integer.parseInt(reader.readLine().toString());
            int longest;
            AAAAAA prob;
            for (int n = 0; n < NUM_INPUT; n++) {
                dims = reader.readLine().split(" ");
                rows = Integer.parseInt(dims[0]);
                cols = Integer.parseInt(dims[1]);
                int mat[][] = new int[rows][cols];
                int mat2[][] = new int[rows][cols];
                int mat3[][] = new int[rows][cols];
                for (int r = 0; r < rows; r++) {
                    line = reader.readLine();
                    for (int c = 0; c < cols; c++) {
                        if (line.charAt(c) == '.') {
                            mat[r][c] = 0;
                            mat2[r][c] = 0;
                            mat3[r][c] = 0;
                        }
                        else if (line.charAt(c) == '#') {
                            mat[r][c] = -1;
                            mat2[r][c] = -1;
                            mat3[r][c] = -1;
                        }
                    }
                }
                prob = new AAAAAA();
                longest = prob.longest_path(mat, mat2, mat3, rows, cols);
                //System.out.printf("Case %d: %d\n", n+1, longest);
                writer.write("Case " + Integer.toString(n+1) + ": " + Integer.toString(longest) + '\n');
            }
            reader.close();
            writer.close();
        } catch (IOException x) {
            System.err.format("IOException: %s%n", x);
        }
    }

}
