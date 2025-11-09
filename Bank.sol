
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Bank {
    
    address public accountOwner;

    constructor() {
        accountOwner = msg.sender;
    }

    // Deposit money into the contract
    function deposit() public payable {
        require(msg.value > 0, "Amount should be greater than 0!");
    }

    // Withdraw money from the contract
    function withdraw(uint amount) public {
        require(msg.sender == accountOwner, "You are not the account owner!");
        require(amount <= address(this).balance, "Insufficient balance!");
        payable(msg.sender).transfer(amount);
    }

    // Show balance of the account
    function showBalance() public view returns (uint) {
        return address(this).balance;
    }
}
