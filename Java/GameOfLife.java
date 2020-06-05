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
  int ROW = 70;
  int COLUMN = 70;
  Random random = new Random();
  int updatedGrid[][] = new int[ROW][COLUMN];

  public GameOfLife() {
    DrawCells cellsComp = new DrawCells();
    this.setTitle("Game Of Life: Java");
    this.setSize(PIXELSIZE * ROW, PIXELSIZE * COLUMN);
    this.setLocationRelativeTo(null);
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    this.add(cellsComp);
    this.setVisible(true);
  }

  private class DrawCells extends JComponent {
    int x;
    int y;
    int grid[][] = new int[ROW][COLUMN];

    public void createGrid() {
      for (int i = 0; i < grid.length; i++) {
        for (int j = 0; j < grid[i].length; j++) {
          grid[i][j] = random.nextInt(2);
        }
      }
      //System.out.println(Arrays.deepToString(grid).replace("], ", "]\n"));
    }

    public void paintComponent(Graphics g) {
      super.paintComponent(g);
      createGrid();
      Graphics2D g2 = (Graphics2D) g;
      for (int i = 0; i < ROW; i++) {
        for (int j = 0; j < COLUMN; j++) {
          if (grid[i][j] == 1) {
            g2.setColor(Color.RED);
            g2.fillRect(i * PIXELSIZE, j * PIXELSIZE, PIXELSIZE, PIXELSIZE);
          }
        }
      }
    }
  }

  public static void main(String[] args) {
    GameOfLife gol = new GameOfLife();
  }
}
