import javax.swing.JFrame;
import java.util.Random;
import java.util.Arrays;
import javax.swing.JComponent;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Rectangle;
import java.awt.Color;
import java.awt.event.ActionListener;
import java.awt.event.ActionEvent;
import java.awt.event.*;
import javax.swing.*;
import java.awt.BorderLayout;

public class GameOfLife extends JFrame {

  int PIXELSIZE = 10;
  int ROW = 75;
  int COLUMN = 75;
  Random random = new Random();
  JButton start;

  public GameOfLife() {
    JPanel panel = new JPanel();
    DrawCells cellsComp = new DrawCells();
    start = new JButton("Start");
    start.addActionListener(cellsComp);
    panel.setLayout(new BorderLayout());
    start.setToolTipText("Click to start game of life");
    this.setTitle("Game Of Life: Java");
    this.setSize(PIXELSIZE * ROW, PIXELSIZE * COLUMN);
    this.setLocationRelativeTo(null);
    this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    panel.add(start, BorderLayout.SOUTH);
    panel.add(cellsComp, BorderLayout.CENTER);
    this.add(panel);
    this.setVisible(true);
  }

  private class DrawCells extends JComponent implements ActionListener {
    int x;
    int y;
    int grid[][] = new int[ROW][COLUMN];
    int updatedGrid[][] = new int[ROW][COLUMN];

    public void createGrid() {
      for (int i = 0; i < grid.length; i++) {
        for (int j = 0; j < grid[i].length; j++) {
          grid[i][j] = random.nextInt(2);
        }
      }
    }

    public void applyRules() {
      for (int i = 1; i < ROW - 1; i++) {
        for (int j = 1; j < COLUMN - 1; j++) {
          int neighboursCount = 0; // used to count the neighbours of each cell

          neighboursCount += grid[i-1][j-1]; // top left
          neighboursCount += grid[i][j-1]; // top center
          neighboursCount += grid[i+1][j-1]; // top right

          neighboursCount += grid[i-1][j]; // middle left
          neighboursCount += grid[i+1][j]; // middle right

          neighboursCount += grid[i-1][j+1]; // top left
          neighboursCount += grid[i][j+1]; // top center
          neighboursCount += grid[i+1][j+1]; // top right

          // Game of Life rules:

          // Alive cells:
          if (grid[i][j] == 1) {
            // rule 1 any live cell with fewer than two live neighboours dies, as if by underpopulation
            if (neighboursCount < 2) {
              updatedGrid[i][j] = 0;
            }
            // rule 2 any live cell with two or three live neighbours, lives on to the generation
            else if (neighboursCount == 2 || neighboursCount == 3) {
              updatedGrid[i][j] = 1;
            }
            // rule 3 any live cell with more than three live neighbours dies, as if by overpopulation
            else if (neighboursCount > 3 && neighboursCount <= 8) {
              updatedGrid[i][j] = 0;
            }
            else {
              updatedGrid[i][j] = 0;
            }
          }
          // Dead cells
          else if (grid[i][j] == 0) {
            // rule 4 any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction
            if (neighboursCount == 3) {
              updatedGrid[i][j] = 1;
            }
            else {
              updatedGrid[i][j] = 0;
            }
          }
        }
      }
      for (int i = 0; i < ROW; i++) {
        for (int j = 0; j < COLUMN; j++) {
          grid[i][j] = updatedGrid[i][j];
        }
      }
    }

    public void paintComponent(Graphics g) {
      super.paintComponent(g);
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

  Timer animation;
  public void actionPerformed(ActionEvent e) {
    if (e.getSource() == start && animation == null) {
        createGrid(); 
        int delay = 100; //milliseconds
        ActionListener taskPerformer = new ActionListener() {
            public void actionPerformed(ActionEvent evt) {
                applyRules();
                repaint();
            }
        };
        animation = new Timer(delay, taskPerformer);
        animation.start();
      }
    }
  }

  public static void main(String[] args) {
    GameOfLife gol = new GameOfLife();
  }
}
