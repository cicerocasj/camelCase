package org.camelCase;


import static org.junit.Assert.*;

import org.junit.Test;

public class TestCamelCase {
	
	@Test
	public void testAcelerar(){
		String c = CamelCase.getOriginal();
		assertEquals("", c);
	}
}
