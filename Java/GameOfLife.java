import javax.swing.JFrame;
import java.util.Random;
import java.util.Arrays;

public class GameOfLife extends JFrame {

  int row = 700;
  int column = 700;
  Random random = new Random();
  int grid[][] = new int[row][column];
  int updatedGrid[][];

  public GameOfLife() {
    this.setTitle("Game Of Life: Java");
    this.setSize(row, column);
    this.setLocationRelativeTo(null);
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    this.setVisible(true);
  }

  public int[][] createGrid() {
    for (int i = 0; i < grid.length; i++) {
      for (int j = 0; j < grid[i].length; j++) {
        grid[i][j] = random.nextInt(2);
      }
    }
    System.out.println(Arrays.deepToString(grid).replace("], ", "]\n"));
    return grid;
  }

  public static void main(String[] args) {
    GameOfLife gol = new GameOfLife();
    gol.createGrid();
  }
}
