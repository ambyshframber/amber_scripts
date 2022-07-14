#/usr/bin/env lua

Total = 0
while true do
    local x  = math.random(1,6)
    if x == 6 then
        break
    end
    Total = Total + x
end
print(Total)
