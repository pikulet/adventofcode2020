package main

import (
    "fmt"
    "io/ioutil"
    "strconv"
    "strings"
    "sort"
)

func readInput() []int {
    data, err := ioutil.ReadFile("01-input")
    if err != nil {
        panic(err)
    }
    
    lines := strings.Split(string(data), "\n")
    lines = lines[:len(lines) - 1]
    nums := make([]int, 0, len(lines))

    for _, l := range lines {
        n, _ := strconv.Atoi(l)
        nums = append(nums, n)
    }

    return nums
}

func partA(nums []int, target int) int {
    seenNumbers := make(map[int]bool)

    for _, n := range nums {
        required := target - n
        if seenNumbers[required] {
            // Found solution
            answer := required * n
            return answer
        }

        seenNumbers[n] = true
    }

    panic("No solution found.")
}

func partB(nums []int, target int) int {
    sort.Ints(nums)
    
    for i := 0; i < len(nums) - 2; i++ {
        required := target - nums[i]
        left := i + 1
        right := len(nums) - 1
        for left < right {
            if nums[left] + nums[right] == required {
                // Found solution
                answer := nums[i] * nums[left] * nums[right]
                return answer
            } else if nums[left] + nums[right] < required {
                left++
            } else {
                right--
            }
        }
    }

    panic("No solution found.")
}

func main() {
    nums := readInput()
    target := 2020

    ansA := partA(nums, target)
    fmt.Printf("Solution for A: %d\n", ansA)
    ansB := partB(nums, target)
    fmt.Printf("Solution for B: %d\n", ansB)
}

