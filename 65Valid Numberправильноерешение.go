import "unicode"

func isNumber(s string) bool {
    hasDigit := false
    hasDot := false
    hasE := false

    for i, ch := range s {
        if ch == '+' || ch == '-' {
            if i > 0 && (s[i-1] != 'e' && s[i-1] != 'E') {
                return false
            }
        } else if ch == '.' {
            if hasDot || hasE {
                return false
            }
            hasDot = true
        } else if ch == 'e' || ch == 'E' {
            if hasE || !hasDigit {
                return false
            }
            hasE = true
            hasDigit = false
        } else if unicode.IsDigit(ch) {
            hasDigit = true
        } else {
            return false
        }
    }

    return hasDigit
}
