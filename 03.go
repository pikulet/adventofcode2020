package main

import (
    "fmt"
    "io/ioutil"
)

tree byte := byte("#")
areaMap []string
width int
height int

func readInput() {
    data, err := ioutil.ReadFile("03-input")
    if err != nil { panic (err) }
    areaMap = strings.split(string(data), "\n")
    width = len(areaMap[0])
    height = len(areaMap)
}

func getNextX(x, ruleX) int {
    return (x + ruleX) % width
}

func getNextY(y, ruleY) int {
    return (y + ruleY)
}

func isPastBottom(y) bool {
    return y > height - 1
}

func isTree(x, y) bool {
    return areaMap[y][x] == tree
}

func countTrees(ruleX, ruleY) int {
    x := 0
    y := 0

    count := 0
    for !isPastBottom(y) {
        if isTree(x, y) {
            count++
        }
        x = getNextX(x, ruleX)
        y = getNextY(y, ruleY)
    }

    return count
}

rules := [][]int {
    {1, 1},
    {3, 1},
    {5, 1},
    {7, 1},
    {1, 2}
}

func main() {
    readInput()
    product := 1
    for _, rule := range rules {
        ruleX := rule[0]
        ruleY := rule[1]
        num_trees := countTrees(ruleX, ruleY)
        fmt.printf("r %d, d %d: %d trees found", ruleX, ruleY, num_trees)

        product *= num_trees
    }

    fmt.printf("Total produdct: %d", product)
}
