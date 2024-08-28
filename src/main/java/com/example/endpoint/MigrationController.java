package com.example.endpoint;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;

public class MigrationController {
  @PostMapping("/migrate")
  public ResponseEntity<String> migrate(@RequestBody MigrationRequest request) {
    if (!request.isValid()) {
      return new ResponseEntity<>("Invalid request", HttpStatus.BAD_REQUEST);
    }
    MigrationService service = new MigrationService();
    String response = service.migrate(request);
    return new ResponseEntity<>(response, HttpStatus.OK);
  }
}