/**
 * Main class for the Task-1 project
 * Demonstrates basic Java functionality and serves as an entry point
 */
public class Main {
    
    /**
     * Main method - entry point of the application
     * @param args command line arguments
     */
    public static void main(String[] args) {
        System.out.println("Welcome to Task-1 Project!");
        System.out.println("This is a multi-language contribution repository.");
        
        // Demonstrate some basic functionality
        greetUser("Contributor");
        showProjectInfo();
    }
    
    /**
     * Greets a user with a personalized message
     * @param name the name of the user to greet
     */
    public static void greetUser(String name) {
        System.out.println("Hello, " + name + "! Thank you for your interest in contributing.");
    }
    
    /**
     * Displays information about the project
     */
    public static void showProjectInfo() {
        System.out.println("\n=== Project Information ===");
        System.out.println("Languages: Java, Python, HTML");
        System.out.println("Purpose: Demonstration and learning");
        System.out.println("Contributions: Welcome!");
        System.out.println("Check README.md and CONTRIBUTING.md for more details.");
    }
}