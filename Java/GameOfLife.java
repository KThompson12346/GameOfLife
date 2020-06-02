import javax.swing.JFrame;
import java.util.Random;
import java.util.Arrays;
import javax.swing.JComponent;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.Color;

public class GameOfLife extends JFrame {

  int PIXELSIZE = 10;
  int ROW = 700;
  int COLUMN = 700;
  Random random = new Random();
  int grid[][] = new int[ROW][COLUMN];
  int updatedGrid[][] = new int[ROW][COLUMN];

  public GameOfLife() {
    this.setTitle("Game Of Life: Java");
    this.setSize(ROW, COLUMN);
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
    //System.out.println(Arrays.deepToString(grid).replace("], ", "]\n"));
    return grid;
  }

  public static void main(String[] args) {
    GameOfLife gol = new GameOfLife();
  }
}

public class DrawCells extends JComponent {
  public void paintComponent(Graphics g) {
    Graphics2D g2 = (Graphics2D) g;

  }
}
