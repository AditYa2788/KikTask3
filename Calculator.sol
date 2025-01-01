// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;
contract Calculator{
    uint256 result=0;
    function add(uint256 a) public{
        result=result+a;
    }

    function subtract(uint256 a) public{
        result=result-a;
    }
    function multiply(uint256 a) public{
        result=result*a;
    }
    function exponent(uint256 a)public{
        result=result**a;
    } 
    function divide(uint256 a) public{
        result=result/a;
    }
    function get() public view returns(uint256){
        return result;
    }
}
