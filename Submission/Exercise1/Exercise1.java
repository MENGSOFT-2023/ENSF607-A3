import java.sql.*;

public class Exercise1 {
	//JDBC connection details
	static final String JDBC_url = "jdbc:mysql://localhost:3306/Lab3Ex1";
	static final String JDBC_user = "JuanCelis";
	static final String JDBC_password = "MySQL@1";

	public static void main(String[] args) {
//		making connection to database through JDBC driver and adding the jar file into the reference libraries 
		try(Connection connection = DriverManager.getConnection(JDBC_url, JDBC_user, JDBC_password)){
			//get all students from the database and display their attributes
			System.out.print(" --- All Students --- ");
			ResultSet students = connection.createStatement().executeQuery("SELECT * FROM Student");
			while(students.next()) {
				System.out.println("\nStudent ID: " + students.getString("StudentID") + 
									"\nName: " + students.getString("FirstName") + " " + students.getString("LastName") + 
									"\nLocation: " + students.getString("Location"));
			}
			
			//get all courses from the database and display their attributes
			System.out.println("\n --- All Courses --- ");
			ResultSet courses = connection.createStatement().executeQuery("SELECT * FROM Course");
			while(courses.next()) {
				System.out.println("\nCourse ID: " + courses.getString("CourseID") + 
									"\nCourse Name: " + courses.getString("CourseName") + " Course Title: " + courses.getString("CourseTitle"));
			}
			
			//get all registration from the database and display their attributes
			System.out.println("\n --- All Registrations --- ");
			ResultSet registrations = connection.createStatement().executeQuery("SELECT * FROM Registration");
			while(registrations.next()) {
				System.out.println("\nRegistration ID: " + registrations.getString("RegistrationID") + 
									"\nCourseID: " + registrations.getString("CourseID") + 
									"\nStudentID: " + registrations.getString("StudentID"));
			}
			
			
		} catch (SQLException e) {
			// Handle SQL exceptions
			e.printStackTrace();
		}

	}

}
