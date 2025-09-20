#!/usr/bin/env python3
"""
Object-Oriented Programming demonstration for Task-1 project.
This file showcases basic OOP concepts in Python.
"""


class ProjectInfo:
    """
    A class to represent information about the Task-1 project.
    Demonstrates basic OOP concepts like encapsulation and methods.
    """
    
    def __init__(self, name="Task-1", languages=None, purpose="Learning and contribution"):
        """
        Initialize the ProjectInfo object.
        
        Args:
            name (str): Name of the project
            languages (list): List of programming languages used
            purpose (str): Purpose of the project
        """
        self.name = name
        self.languages = languages if languages else ["Java", "Python", "HTML"]
        self.purpose = purpose
        self.contributors = []
    
    def add_contributor(self, contributor_name):
        """
        Add a contributor to the project.
        
        Args:
            contributor_name (str): Name of the contributor
        """
        if contributor_name not in self.contributors:
            self.contributors.append(contributor_name)
            print(f"Welcome, {contributor_name}! Thank you for contributing to {self.name}.")
        else:
            print(f"{contributor_name} is already a contributor to {self.name}.")
    
    def display_info(self):
        """Display comprehensive information about the project."""
        print(f"\n=== {self.name} Project Information ===")
        print(f"Purpose: {self.purpose}")
        print(f"Languages: {', '.join(self.languages)}")
        print(f"Contributors: {len(self.contributors)}")
        if self.contributors:
            print(f"  - {', '.join(self.contributors)}")
        print("Status: Open for contributions!")
    
    def get_contribution_tips(self):
        """Provide tips for new contributors."""
        tips = [
            "Read the README.md file thoroughly",
            "Check the CONTRIBUTING.md for guidelines",
            "Follow the code style conventions",
            "Write meaningful commit messages",
            "Test your changes before submitting",
            "Be respectful and follow the Code of Conduct"
        ]
        
        print("\n=== Contribution Tips ===")
        for i, tip in enumerate(tips, 1):
            print(f"{i}. {tip}")


class Contributor:
    """
    A class to represent a project contributor.
    """
    
    def __init__(self, name, skills=None):
        """
        Initialize a Contributor object.
        
        Args:
            name (str): Name of the contributor
            skills (list): List of programming skills
        """
        self.name = name
        self.skills = skills if skills else []
        self.contributions = 0
    
    def introduce(self):
        """Introduce the contributor."""
        print(f"\nHi! I'm {self.name}.")
        if self.skills:
            print(f"My skills include: {', '.join(self.skills)}")
        print(f"I have made {self.contributions} contributions so far.")
    
    def make_contribution(self):
        """Record a contribution."""
        self.contributions += 1
        print(f"{self.name} made a contribution! Total contributions: {self.contributions}")


def main():
    """
    Main function to demonstrate the OOP concepts.
    """
    print("Welcome to the Task-1 Project OOP Demo!")
    
    # Create a project instance
    project = ProjectInfo()
    project.display_info()
    
    # Create some contributors
    contributor1 = Contributor("Alice", ["Python", "Java"])
    contributor2 = Contributor("Bob", ["HTML", "CSS", "JavaScript"])
    
    # Add contributors to the project
    project.add_contributor(contributor1.name)
    project.add_contributor(contributor2.name)
    
    # Let contributors introduce themselves
    contributor1.introduce()
    contributor2.introduce()
    
    # Make some contributions
    contributor1.make_contribution()
    contributor2.make_contribution()
    contributor1.make_contribution()
    
    # Display updated project info
    project.display_info()
    
    # Show contribution tips
    project.get_contribution_tips()


if __name__ == "__main__":
    main()