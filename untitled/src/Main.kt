import java.io.File

fun main() {
    val text = File("C:/Users/").readText()

    var word = ""
    var lineNumber = 1
    var columnNumber = 0

    text.forEach { char ->
        when {
            char.isWhitespace() -> {
                if (word.isNotEmpty()) {
                    printWordOrNumberOrLetter(word, "$lineNumber:${columnNumber - word.length}")
                    word = ""
                }
                if (char == '\n') {
                    println("NEW_LINE")
                    lineNumber++
                    columnNumber = 0
                }
                columnNumber++
            }
            char == '|' -> {
                if (word.isNotEmpty()) {
                    printWordOrNumberOrLetter(word, "$lineNumber:${columnNumber - word.length}")
                    word = ""
                }
                println("DELIMITER: $char at $lineNumber:$columnNumber")
                columnNumber++
            }
            isSpecialCharacter(char) -> {
                if (word.isNotEmpty()) {
                    printWordOrNumberOrLetter(word, "$lineNumber:${columnNumber - word.length}")
                    word = ""
                }
                println("SPECIAL_CHARACTER: $char at $lineNumber:$columnNumber")
                columnNumber++
            }
            isPunctuation(char) && char != '\'' -> {
                if (word.isNotEmpty()) {
                    printWordOrNumberOrLetter(word, "$lineNumber:${columnNumber - word.length}")
                    word = ""
                }
                println("PUNCTUATION: $char at $lineNumber:$columnNumber")
                columnNumber++
            }
            else -> {
                word += char
                columnNumber++
            }
        }
    }
    if (word.isNotEmpty()) {
        printWordOrNumberOrLetter(word, "$lineNumber:${columnNumber - word.length}")
    }
    println("END_OF_LINE")
}

fun printWordOrNumberOrLetter(word: String, position: String) {
    when {
        word.isNumeric() -> println("NUMBER: $word at $position")
        word.length == 1 && word[0].isLetter() -> println("LETTER: $word at $position")
        word == "'" -> println("SPECIAL_CHARACTER: $word at $position")
        else -> println("WORD: $word at $position")
    }
}

fun String.isNumeric(): Boolean {
    return this.matches("\\d+".toRegex())
}

fun isPunctuation(char: Char): Boolean {
    val punctuation = listOf(',', '.', '!', '?', ':', ';', '-', '(', ')', '[', ']', '{', '}', '\'', '\"')
    return punctuation.contains(char)
}

fun isSpecialCharacter(char: Char): Boolean {
    val specialCharacters = listOf('@', '#', '$', '%', '^', '&', '*', '_', '+', '=', '/', '\\', '~', '`')
    return specialCharacters.contains(char)
}