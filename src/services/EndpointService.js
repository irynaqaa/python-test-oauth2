export class EndpointService {
  constructor(private db: any) {}

  async performBusinessLogic(data: any): Promise<any> {
    try {
      if (!data || typeof data !== 'object') {
        throw new Error('Invalid input data');
      }

      const result = await this.db.query(data);
      return result;
    } catch (error) {
      console.error(error);
      throw error;
    }
  }
}