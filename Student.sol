// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract StudentData {

    struct Student {
        uint rollNo;
        string name;
        uint marks;
    }

    Student[] public students;

    // Add new student
    function addStudent(uint _rollNo, string memory _name, uint _marks) public {
        students.push(Student(_rollNo, _name, _marks));
    }

    // Show total number of students
    function totalStudents() public view returns (uint) {
        return students.length;
    }

    // Receive Ether
    receive() external payable {}

    // Fallback function
    fallback() external payable {}
}
