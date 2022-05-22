import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TestService {
  apiUrl: string = 'http://127.0.0.1:5000';
  constructor(private http: HttpClient) { }

  getCall(): Observable<any> {
    return this.http.get(this.apiUrl + '/questions')
  }
}
