import java.util.Scanner;
import java.io.File;

public class Anything {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the folder path to organize: ");
        String folderPath = scanner.nextLine();
        
        File folder = new File(folderPath);
        if (folder.exists() && folder.isDirectory()) {
            
            System.out.println("Organizing folder: " + folderPath);
            
        } else {
            System.out.println("Invalid folder path. Please try again.");
        }
        
        scanner.close();
    }
}