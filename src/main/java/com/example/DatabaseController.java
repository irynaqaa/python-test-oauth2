package com.example;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class DatabaseController {
    private Connection connection;

    public DatabaseController(String url, String username, String password) throws SQLException {
        connection = DriverManager.getConnection(url, username, password);
    }

    public void createData(String data) throws SQLException {
        PreparedStatement statement = connection.prepareStatement("INSERT INTO table_name (column_name) VALUES (?)");
        statement.setString(1, data);
        statement.executeUpdate();
    }

    public String readData() throws SQLException {
        PreparedStatement statement = connection.prepareStatement("SELECT column_name FROM table_name");
        ResultSet resultSet = statement.executeQuery();
        if (resultSet.next()) {
            return resultSet.getString(1);
        }
        return null;
    }

    public void updateData(String data) throws SQLException {
        PreparedStatement statement = connection.prepareStatement("UPDATE table_name SET column_name = ? WHERE condition");
        statement.setString(1, data);
        statement.executeUpdate();
    }

    public void deleteData() throws SQLException {
        PreparedStatement statement = connection.prepareStatement("DELETE FROM table_name WHERE condition");
        statement.executeUpdate();
    }
}