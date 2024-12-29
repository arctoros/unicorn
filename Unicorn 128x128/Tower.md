const null reg5
const toggle 5

# setup
add input null reg0
add input null reg1
add input null reg2
add input null reg3

label func_move
equali 0 reg0 if_case

label else_case
# save stack
push reg0 null null
push reg1 null null
push reg2 null null
push reg3 null null

# disk_nr-1, source, spare, dest
addi 1 null reg4
sub reg0 reg4 reg0
add reg2 null reg4
add reg3 null reg2
add reg4 null reg3
 
call clock null func_move

# move disk from source to dest
add reg1 null output
addi toggle null output
add reg2 null output
addi toggle null output

# disk_nr-1, spare, dest, source
push reg0 null null
push reg1 null null
push reg2 null null
push reg3 null null

addi 1 null reg4
sub reg0 reg4 reg0
add reg1 null reg4
add reg3 null reg1
add reg4 null reg3

call clock null func_move

true null null end_case

label if_case
# move disk from source to dest
add reg1 null output
addi toggle null output
add reg2 null output
addi toggle null output

label end_case
ret null null reg4
ret null null reg3
ret null null reg2
ret null null reg1
ret null null reg0

add reg4 null clock