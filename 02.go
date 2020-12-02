package main

import (
    "fmt"
    "io/ioutil"
    "strconv"
    "strings"
)

type PasswordPolicy struct {
    minVal int
    maxVal int
    letter string
    pw string
}

func readInput() []PasswordPolicy {
    data, err := ioutil.ReadFile("02-input")
    if err != nil {
        panic(err)
    }

    lines := strings.Split(string(data), "\n")
    lines = lines[:len(lines) - 1]
    pws := make([]PasswordPolicy, 0, len(lines))

    for _, line := range lines {
        lineSplit := strings.Split(line, ":")
        policy := lineSplit[0]
        pw := lineSplit[1]
        pw = pw[1:]
        letter := string(policy[len(policy) - 1])
        minMaxVal := strings.Split(strings.Split(policy, " ")[0], "-") 
        minVal, _ := strconv.Atoi(minMaxVal[0])
        maxVal, _ := strconv.Atoi(minMaxVal[1])
        pwPolicy := PasswordPolicy{minVal, maxVal, letter, pw}
        pws = append(pws, pwPolicy)
    }

    return pws
}

func partA(pws []PasswordPolicy) int {
    
    result := 0

    for _, pwPolicy := range pws {
        count := strings.Count(pwPolicy.pw, pwPolicy.letter)
        if pwPolicy.minVal <= count && count <= pwPolicy.maxVal {
            result += 1
        }
    }

    return result
}

func partB(pws []PasswordPolicy) int {

    result := 0

    for _, pwPolicy := range pws {
        letter1 := string(pwPolicy.pw[pwPolicy.minVal - 1])
        letter2 := string(pwPolicy.pw[pwPolicy.maxVal - 1])
        if letter1 == pwPolicy.letter && letter2 != pwPolicy.letter {
            result += 1
        } else if letter1 != pwPolicy.letter && letter2 == pwPolicy.letter {
            result += 1
        }
    }

    return result
}

func main() {
    pws := readInput()
    ansA := partA(pws)
    fmt.Printf("Solution for A: %d\n", ansA)
    ansB := partB(pws)
    fmt.Printf("Solution for B: %d\n", ansB)

}

