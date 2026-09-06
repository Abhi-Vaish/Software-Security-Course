fn main() {
    let mut buffer = [0u8; 32];
    let input = b"AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA";

    for i in 0..input.len() {
        buffer[i] = input[i];
    }

    println!("Boundary test completed");
}
